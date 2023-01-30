import java.net.*;
import java.io.*;

public class Server{
    private Socket clientSocket=null;
    private ServerSocket serverSocket=null;
    private DataInputStream in=null;
    private DataOutputStream out=null;
    public Server(int port){
        try{
            serverSocket= new ServerSocket(port);
            System.out.println("Waiting for client to send file");
            clientSocket=serverSocket.accept();
            System.out.println("Client connected! Printing file and echoing back to client.");
            in=new DataInputStream(clientSocket.getInputStream());
            out=new DataOutputStream(clientSocket.getOutputStream());
            int count=0;
            byte[] buffer=new byte[4096];
            while((count=in.read(buffer))>0){
                out.write(buffer,0,count);
                String recv=new String(buffer);
                System.out.print(recv);
            }
            System.out.println("Closing socket and freeing resources");
            clientSocket.close();
            in.close();
            out.close();
            System.out.println("Closing server");
            serverSocket.close();
        }
        catch(IOException e){
            System.err.println(e);
        }
        
    }
    public static void main(String args[]){
        Server s=new Server(1234);
    }
}