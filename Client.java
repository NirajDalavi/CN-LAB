import java.net.*;
import java.io.*;
public class Client {
    private Socket serverSocket=null;
    private DataInputStream in=null;
    private DataOutputStream out=null;
    public Client(String host,int port,String infilePath,String outfilePath){
        try{
            serverSocket=new Socket(host,port);
            in=new DataInputStream(serverSocket.getInputStream());
            out=new DataOutputStream(serverSocket.getOutputStream());
            File sendFile=new File(infilePath);
            long filelength=sendFile.length();
            if(filelength>Integer.MAX_VALUE){
                throw new Exception("File length too large");

            }
            System.out.println("Sending file to server");
            FileInputStream fin=new FileInputStream(sendFile);
            int count=0;
            byte[] buffer=new byte[4096];
            while((count=fin.read(buffer))>0){
                out.write(buffer,0,count);
                String snd=new String(buffer);
                System.out.print(snd);
            }
            System.out.println("Listening for echo from server...");
            File recvFile=new File(infilePath);
            FileOutputStream fout=new FileOutputStream(recvFile);
            long remainingFilelength=filelength;
            while((count=in.read(buffer))>0){
                fout.write(buffer,0,count);
                String recv=new String(buffer);
                System.out.print(recv);
                remainingFilelength-=count;
                if(remainingFilelength==0)
                    break;

            }
            System.out.println("Saved file in "+outfilePath);
            System.out.println("Closing socket and freeing resources...");
            fin.close();
            fout.close();
            in.close();
            out.close();
            serverSocket.close();

        }
        catch(UnknownHostException e){
            System.err.println(e);
        }
        catch(IOException e){
            System.err.println(e);
        }
        catch(Exception e){
            System.err.println(e);
        }
        
    }
    public static void main(String args[]){
        Client c=new Client("127.0.0.1",1234,"sendFile","recvFile");
    }
    
}
