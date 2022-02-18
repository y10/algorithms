import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

import utils.Test;

public class nr {

    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        // Test.testit("abcab", 'c', nr::nonRepeating);
        Test.testit(() -> nonRepeating("abcab"), 'c'); // should return 'c'
        Test.testit(() -> nonRepeating("abab"), null); // should return null
        Test.testit(() -> nonRepeating("aabbbc"), 'c'); // should return 'c'
        Test.testit(() -> nonRepeating("aabbdbc"), 'd'); // should return 'd'
    }

    // Implement your solution below.
    public static Character nonRepeating(String s) {
        HashMap<Character, Integer> uniqueChars = new LinkedHashMap<Character, Integer>();

        for (Character c : s.toCharArray()) {
            uniqueChars.put(c, uniqueChars.getOrDefault(c, 0) + 1);
        }

        for (Map.Entry<Character,Integer> entry: uniqueChars.entrySet()) {
            if (entry.getValue() == 1)
                return entry.getKey();
        }

        return null;
    }
}
