import java.util.HashMap;

class Solution {
	
	
	
	public static void main(String args[]) {
		String[] words = new String[] {"cat","bt","hat","tree"};
		String chars = "atach";
		
		System.out.println(countCharacters(words, chars));
	}
	
	
    public static int countCharacters(String[] words, String chars) {
        HashMap<Character, Integer> charCount = charCount(chars);
        int result = 0;
        for(String word : words){
            if(formableWord(word, charCount)) result += word.length();
    }
    return result;
    }
    
    public static HashMap<Character, Integer> charCount(String word){
        HashMap<Character, Integer> charCount = new HashMap<Character, Integer>();
        for(int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if(!charCount.containsKey(c)){
                charCount.put(c,1);
            }
            else{
                charCount.put(c,charCount.get(c)+1);
            }
    }
    System.out.println(charCount);
    return charCount;
}

public static boolean formableWord(String word,  HashMap<Character, Integer> chars){
    HashMap<Character, Integer> wordChars = charCount(word);
    for(int i = 0; i < word.length(); i++){
                char c = word.charAt(i);
                if(chars.containsKey(c) && wordChars.containsKey(c)){
                    if(chars.get(c) < wordChars.get(c)) return false;
                }
                else{
                    return false;
                }
            }
            return true;
        }
}
