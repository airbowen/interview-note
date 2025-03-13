public class MinimumCopies {

    public static int minimumCopies(String source, String target) {
        int sourceLen = source.length();
        int targetLen = target.length();
        
        int copyCount = 1;  // 至少需要一次复制源字符串
        int sourceIndex = 0; // 用来遍历源字符串
        int targetIndex = 0; // 用来遍历目标字符串

        // 遍历目标字符串
        while (targetIndex < targetLen) {
            // 如果当前源字符串的字符和目标字符串的字符匹配
            if (source.charAt(sourceIndex) == target.charAt(targetIndex)) {
                targetIndex++;  // 匹配成功，目标字符串的指针向前移动
            }
            
            sourceIndex++;  // 移动源字符串的指针
            
            // 如果源字符串遍历完了，说明需要再复制一次源字符串
            if (sourceIndex == sourceLen) {
                copyCount++;  // 增加复制次数
                sourceIndex = 0;  // 重置源字符串的指针
            }
        }

        return copyCount;
    }

    public static void main(String[] args) {
        // 测试用例
        System.out.println("Minimum copies for source = 'ab' and target = 'b': " + minimumCopies("ab", "b"));  // 输出: 1
        System.out.println("Minimum copies for source = 'abcd' and target = 'dcba': " + minimumCopies("abcd", "dcba"));  // 输出: 4
        System.out.println("Minimum copies for source = 'ab' and target = 'ab': " + minimumCopies("ab", "ab"));  // 输出: 1
        System.out.println("Minimum copies for source = 'abc' and target = 'cabcabc': " + minimumCopies("abc", "cabcabc"));  // 输出: 3
    }
}
