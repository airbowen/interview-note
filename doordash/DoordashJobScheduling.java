import java.util.Arrays;
class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][];
        for (int i = 0; i < n; i++) {
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        }
        Arrays.sort(jobs, (a, b) -> a[1] - b[1]); // 按照结束时间排序

        int[] f = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int j = search(jobs, i, jobs[i][0]);
            f[i + 1] = Math.max(f[i], f[j + 1] + jobs[i][2]);
        }
        return f[n];
    }

    // 返回 endTime <= upper 的最大下标
    private int search(int[][] jobs, int right, int upper) {
        int left = -1;
        while (left + 1 < right) {
            int mid = (left + right) >>> 1;
            if (jobs[mid][1] <= upper) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return left;
    }
}


public class DoordashJobScheduling {
    public static void main(String[] args) {
        // 测试数据
        int[] startTime = {1, 2, 3, 3};
        int[] endTime = {3, 4, 5, 6};
        int[] profit = {50, 10, 40, 70};

        // 创建 Solution 实例
        Solution solution = new Solution();

        // 调用 jobScheduling 方法并打印结果
        int maxProfit = solution.jobScheduling(startTime, endTime, profit);
        System.out.println("最大收益: " + maxProfit);
    }
}
