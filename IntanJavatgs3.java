
package intanjavatgs3;
import java.util.Scanner;
public class IntanJavatgs3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int panjang, lebar, luas, masukan, r;
        double luas1,phi=3.14;
        float alas,tinggi,luas2;
        
        System.out.println("1.Persegi");
        System.out.println("2.Lingkaran");
        System.out.println("3.Segitiga");
        
        System.out.println("MASUKKAN PILIHAN ANDA : ");
        masukan = input.nextInt();
        
        if(masukan == 1){
            
            System.out.println("msukan panjang : ");
            panjang = input.nextInt();
            
            System.out.println("masukan lebar : ");
            lebar = input.nextInt();
            
            luas = panjang * lebar;
            System.out.println("luas persegi adalah : "+luas);
            
        }
        else if(masukan == 2){
            System.out.println("masukan jari-jari : ");
            r = input.nextInt();
            
            luas1 = phi*r*r;
            System.out.println("luaslingkaran :"+luas1);
            
        }
        else if(masukan == 3){
            System.out.println("masukan nilai alas : ");
            alas = input.nextFloat();
            
            System.out.println("masukan niai tinggi : ");
            tinggi = input.nextFloat();
            
            luas2 = alas*tinggi/2;
            System.out.println("luas segitiga adalah : "+luas2);
        }
        else{
            System.out.println("KODE YANG ANDA MASUKKAN SALAH");
            
        }
        
    }
    
}
