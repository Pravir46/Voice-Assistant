public class SwapWords {
    public static void main(String[] args) {
        String firstWord = "Hello";
        String secondWord = "World";
        System.out.println("Before swapping:");
        System.out.println("First word = " + firstWord);
        System.out.println("Second word = " + secondWord);
        String temp = firstWord;
        firstWord = secondWord;
        secondWord = temp;
        System.out.println("After swapping:");
        System.out.println("First word = " + firstWord);
        System.out.println("Second word = " + secondWord);
    }
}