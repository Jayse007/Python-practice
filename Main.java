public class Main{
    public static void main(String[] args){
        float x= 12.78f;
        int float_conv = (int) x;
        
        if (x <= 18){
            System.out.println("Why are you trying to access this site underaged");
            System.out.println( "Your age is " + float_conv + " and you have to at least be 18 to access this site. Better luck next time. Come back when you are old enough.");
        }
        else {
            System.out.println("Welcome, user. Have a nice visit. Please follow company policies and do not help minors get on this site");
        }
        System.out.println((float_conv> 18f) ? "How is everything, sir or ma. We hope you have a pleasant stay":"This is something we do not smile upon. Do not implicate us like this.");
        
        
        if (float_conv == 12){
            System.out.println("This is a float value.");

        }}
    }



