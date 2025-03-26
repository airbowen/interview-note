/*
clarify questions:


ideas: stack 存后续遍历
1. 最简单就是存储所有的情况，然后一个个返回
这样肯定是不行的
2.懒加载的方式去产生
因为post order是左右中
我们用一个**栈（stack）**来模拟递归过程，并使用两个辅助指针：
current：当前正在访问的节点（从根节点开始）
lastVisited：上一次访问过的节点（用于判断右子树是否访问过）
每次调用 next()：
一直把左孩子压入栈中（模拟递归到最左）。
到达最左后，查看栈顶节点（peek）：
如果栈顶节点有右孩子，并且右孩子还没被访问过 → 转去访问右子树；

否则说明左右子树都访问过，可以访问当前节点（即弹出栈顶并返回该值）。

用 lastVisited 标记刚刚访问过的节点，避免重复访问右子树。

第一个栈：遍历节点时按 根 -> 左 -> 右 的顺序压栈。

第二个栈：将第一个栈的出栈结果压入，最终按后序遍历顺序输出。
*/
import java.util.*;
class Solution {
    class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int x) { val = x; }
    }

    public interface PostOrderBinaryTreeIterator extends Iterator<Integer> {
        public int next();
        public boolean hasNext();
    }
    public class PostOrderIterator implements PostOrderBinaryTreeIterator {
        private Stack<TreeNode> stack = new Stack<>();
        private TreeNode lastVisited = null;
        private TreeNode current;
        @Override
        public boolean hasNext() {
            return current != null || !stack.isEmpty();
        }

        @Override
        public int next() {
            while (true) {
                // 将当前节点的左子结点
                if (current != null) {
                    stack.push(current);
                    current = current.left;
                } else {
                    TreeNode peekNode = stack.peek();
                    //左子结点访问过了
                    //此时看右子节点,因为post-order是左右中
                    //右子节点是右子树中最后访问的
                    //如果上一个访问的节点是右子节点
                    //那么说明右子树访问完了
                    //否则就需要访问右子树
                    if (peekNode.right != null && lastVisited != peekNode.right) {
                        current = peekNode.right;
                    } 
                    //右子树访问完了，访问当前节点
                    else {
                        stack.pop();
                        //记录一下lastVisited
                        lastVisited = peekNode;
                        return peekNode.val;
                    }
                }
            }
        }
    }
  
    public static void main(String[] args) {
  
    }
}
