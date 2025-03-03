"use client"

import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { Search, RefreshCw } from "lucide-react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import CryptoCard from "@/components/crypto-card"
import LoadingSkeleton from "@/components/loading-skeleton"

// Fetch crypto data from CoinGecko API
const fetchCryptoData = async () => {
  const response = await fetch(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h",
  )

  if (!response.ok) {
    throw new Error("Failed to fetch crypto data")
  }

  return response.json()
}

export default function CryptoTracker() {
  const [searchTerm, setSearchTerm] = useState("")

  const { data, isLoading, isError, error, refetch } = useQuery({
    queryKey: ["cryptoData"],
    queryFn: fetchCryptoData,
    staleTime: 60000, // 1 minute
  })

  // Filter cryptocurrencies based on search term
  const filteredCryptos =
    data?.filter(
      (crypto) =>
        crypto.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        crypto.symbol.toLowerCase().includes(searchTerm.toLowerCase()),
    ) || []

  // Get top 5 cryptocurrencies if no search term
  const displayedCryptos = searchTerm ? filteredCryptos : filteredCryptos.slice(0, 5)

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
          <Input
            type="text"
            placeholder="Search cryptocurrencies..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10 bg-gray-800 border-gray-700 text-white"
          />
        </div>
        <Button onClick={() => refetch()} className="bg-indigo-600 hover:bg-indigo-700">
          <RefreshCw size={18} className="mr-2" />
          Refresh Prices
        </Button>
      </div>

      {isLoading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {[...Array(5)].map((_, index) => (
            <LoadingSkeleton key={index} />
          ))}
        </div>
      ) : isError ? (
        <div className="p-6 bg-red-900/30 rounded-lg border border-red-700">
          <p className="text-red-300">Error: {error instanceof Error ? error.message : "Failed to fetch data"}</p>
          <Button
            onClick={() => refetch()}
            variant="outline"
            className="mt-4 border-red-700 text-red-300 hover:bg-red-900/50"
          >
            Try Again
          </Button>
        </div>
      ) : (
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {displayedCryptos.map((crypto) => (
              <CryptoCard key={crypto.id} crypto={crypto} />
            ))}
          </div>

          {searchTerm && displayedCryptos.length === 0 && (
            <div className="p-6 bg-gray-800/50 rounded-lg border border-gray-700 text-center">
              <p className="text-gray-400">No cryptocurrencies found matching "{searchTerm}"</p>
            </div>
          )}
        </>
      )}
    </div>
  )
}

