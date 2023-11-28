package arrayList;

import java.util.ArrayList;

public class Ex02 {
    public static void main(String[] args) {
        ArrayList<String> nameList = new ArrayList<>();
        System.out.println(nameList.isEmpty());
        nameList.add("박한결");
        System.out.println(nameList.isEmpty());
        nameList.add("박시우");
        nameList.add("권동영");
        nameList.add("양준석");
        nameList.add("장연준");
        System.out.println(nameList.size());
        System.out.println(nameList.get(3));
        System.out.println(nameList);

        String removeValue = nameList.remove(2);
        System.out.println(nameList);
        System.out.println(nameList.get(2));
        System.out.println(removeValue);

        System.out.println("일반적인 배열");
        for (int i=0; i < nameList.size(); i++) {
            System.out.println(nameList.get(i));
        }

        System.out.println("for ~ each 문");
        for (String name : nameList) {
            System.out.println(name);
        }
    }
}
