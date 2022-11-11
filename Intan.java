package intan;
import java.util.Scanner;
public class Intan {
public static void main(String[] args) {
    System.out.println("pilih operator yang diinginkan");
    System.out.println("1. penjumlahan");
    System.out.println("2. perkalian");
    System.out.println("3. pengurangan");
    System.out.println("4. pembagian");
    
    Scanner input = new Scanner(System.in);
    System.out.println("masukkan pilihan opeator anda :");
    int pilihan = input.nextInt();
    
    System.out.println("");
    System.out.println("masukan bilangan 1: ");
    int bilangan1 = input.nextInt();
    System.out.println("masukkan bilangan 2: ");
    int bilangan2 = input.nextInt();
    
    
    
    if (pilihan == 1){
        int hasil = bilangan1 + bilangan2;
        System.out.println("hasl penjumlahan bilangan :" + hasil);
    }else if (pilihan == 2){
        int hasil = bilangan1 * bilangan2;
        System.out.println("hasil perkalian bilangan :" + hasil);
    }else if (pilihan == 3){
        int hasil = bilangan1 - bilangan2;
        System.out.println("hasil pengurangan bilangan :" + hasil);
    }else if (pilihan == 4){
        int hasil = bilangan1 / bilangan2;
        System.out.println("hasil pembagia bilangan :" + hasil);
    }
        }
    
}
