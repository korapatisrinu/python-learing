// import java.util.*;



// public class nani{
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         int n = sc.nextInt();
//         int[] scores = new int[n];

//         for (int i = 0; i < n; i++) {
//             scores[i] = sc.nextInt();
//         }

//         Set<Integer> uniqueSet = new HashSet<>();
//         for (int score : scores) {
//             uniqueSet.add(score);
//         }

//         if (uniqueSet.size() < 2) {
//             System.out.println(-1);
//             return;
//         }

//         List<Integer> uniqueList = new ArrayList<>(uniqueSet);
//         Collections.sort(uniqueList, Collections.reverseOrder());

//         System.out.println(uniqueList.get(1));
//     }
// }
import java.util.*;
public class nani{
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int[] arr={1,2,3,4,5};
      int removeIndex=2;
      for(int i=removeIndex;i<arr.length-1;i++){
      arr[i]=arr[i+1];
      }
arr[arr.length-1]=0;
for(int num:arr){
    System.out.print(num +" ");
}
   }}