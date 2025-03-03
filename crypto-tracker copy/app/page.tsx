import CryptoTracker from "@/components/crypto-tracker"

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-2">Crypto Price Tracker</h1>
        <p className="text-gray-300 mb-8">Track live cryptocurrency prices in real-time</p>
        <CryptoTracker />
      </div>
    </main>
  )
}

