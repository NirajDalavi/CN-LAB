//CRC Checksum
import java.util.*;

public class CRC{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter message bits: ");
        String message = in.nextLine();
        System.out.print("Enter the generator: ");
        String generator = in.nextLine();

        int[] data = new int[(2*message.length())-generator.length()+1];
        int[] divisor = new int[generator.length()];
        int[] checksum = new int[(2*message.length())-generator.length()+1];

        for(int i=0;i<message.length();i++)
            data[i] = checksum[i] = Integer.parseInt(message.charAt(i)+"");
        for(int i=message.length();i<data.length;i++)
            data[i]=0;
        for(int i=0;i<generator.length();i++)
                        divisor[i] = Integer.parseInt(generator.charAt(i)+"");

        //Calculation of CRC
        for(int i=0;i<=(data.length-divisor.length);i++){
            if(data[i]==1)
                for(int j=0;j<divisor.length;j++)
                    data[i+j]^=divisor[j];
        }
        for(int i=message.length();i<data.length;i++)
                        checksum[i] = data[i];
        //Display of CRC
        System.out.print("The Checksum code is: ");
        for(int i=0;i<data.length;i++)
            System.out.print(checksum[i]);
        System.out.println();
        //Check for input CRC code
            System.out.print("Enter the recieved Checksum code: ");
                message = in.nextLine();
                
                data = new int[message.length()];
                
                for(int i=0;i<message.length();i++)
                        data[i] = Integer.parseInt(message.charAt(i)+"");
        //Calculation of remainder
        for(int i=0;i<=(data.length-divisor.length);i++){
                        if(data[i]==1)
                                for(int j=0;j<divisor.length;j++)
                                        data[i+j]^=divisor[j];
                }
        //Check for Validity
        boolean valid = true;
        for(int i=0;i<data.length;i++){
                        if(data[i]==1){
                valid = false;
                break;
            }
        }
        if(valid==true)
            System.out.println("Data stream is valid");
        else
            System.out.println("Data stream is invalid. CRC error occurred.");
        in.close();
    }
}
