import { Card, CardContent } from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"

export default function LoadingSkeleton() {
  return (
    <Card className="overflow-hidden border-gray-700 bg-gray-800/50">
      <CardContent className="p-6">
        <div className="flex items-center gap-4 mb-4">
          <Skeleton className="h-12 w-12 rounded-full bg-gray-700" />
          <div className="space-y-2">
            <Skeleton className="h-5 w-32 bg-gray-700" />
            <Skeleton className="h-4 w-16 bg-gray-700" />
          </div>
        </div>

        <div className="space-y-4">
          <div>
            <Skeleton className="h-3 w-16 mb-2 bg-gray-700" />
            <Skeleton className="h-7 w-28 bg-gray-700" />
          </div>

          <div className="flex justify-between">
            <div>
              <Skeleton className="h-3 w-16 mb-2 bg-gray-700" />
              <Skeleton className="h-5 w-16 bg-gray-700" />
            </div>

            <div>
              <Skeleton className="h-3 w-16 mb-2 bg-gray-700" />
              <Skeleton className="h-5 w-16 bg-gray-700" />
            </div>

            <div>
              <Skeleton className="h-3 w-16 mb-2 bg-gray-700" />
              <Skeleton className="h-5 w-16 bg-gray-700" />
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

