/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution863 {
  //Solution to LeetCode Ex.863 https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/?envType=daily-question&envId=2023-12-04
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
    			Queue<TreeNode> q = new LinkedList<>();
    			HashMap<TreeNode,Boolean> visited = new HashMap<>();
    			Map<TreeNode,TreeNode> parents = parentMap(root);
    			int dist = 0;
    			q.add(target);
    			visited.put(target, true);
    			while(!q.isEmpty()) {
    				if(dist == k) break;
    				dist += 1;
    				int n = q.size();
    				for(int i = 0; i < n; i++) {
    					TreeNode node = q.poll();
    					if(node.left != null && visited.get(node.left) == null) {
    						q.add(node.left);
    						visited.put(node.left, true);
    					}
    					if(node.right != null && visited.get(node.right) == null) {
    						q.add(node.right);
    						visited.put(node.right, true);
    					}
    					TreeNode parent = parents.get(node);
    					if(parent != null && visited.get(parent) == null) {
    						q.add(parent);
    						visited.put(parent,true);
    					}
    				}
    				
    			}
    			List<Integer> result = new ArrayList<>();
    			while(!q.isEmpty()) {
    				result.add(q.poll().val);
    			}
    			return result;
    }

    private static Map<TreeNode,TreeNode> parentMap(TreeNode root){
    	Queue<TreeNode> q = new LinkedList<>();
    	Map<TreeNode,TreeNode> parents = new HashMap<>();
    	q.add(root);
			
    	while(!q.isEmpty()) {
    		TreeNode node = q.poll();
    		if(node.left != null) {
    			q.add(node.left);
    			parents.put(node.left, node);
    		}
    		if(node.right != null) {
    			q.add(node.right);
    			parents.put(node.right, node);
    		}
    	}
    	return parents;
    }
}
