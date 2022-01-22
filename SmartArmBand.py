#include <SoftwareSerial.h>
SoftwareSerial pro(7,8);        //RX,TX   회로상 7번-TX핀  8번-RX핀
int check=0;
char a;                         //송수신을 위한 변수
#define sw 3                    //스위치는 3번
#define vi 2                    //진동모터는 번
#define red 5                   //빨간색 led는 5번
#define green 4                 //초록색 led는 4번
void setup(){
  pinMode(vi,OUTPUT);           //진동모터 출력설정
  pinMode(sw,INPUT_PULLUP);     //스위치 입력으로 풀업으로 설정
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  Serial.begin(9600);           //통신 송신 속도설정
  pro.begin(9600);              //통신 수신 속도설정
}
void loop(){
   if(pro.available()){          //수신 정보가 있는지 확인
    a=pro.read();                //수신받은 값을 a에 저장
    Serial.write(a);             //시리얼창에 a에 저장된 메세지 출력
   }
   pro.write('y');
   delay(500);
   if(a=='1'){                          //수신한 a값을 비교
    for(int i=0;i<60;i++){              //아래 for문은 진동5번,빨간LED깜빡이기 5번 수행 후 a는 0으로 설정
      Right_Vi();                       //---------->함수 아래 참고
      if(digitalRead(sw)==LOW){         //송신 정보가 있는지 확인
        pro.write('o');                 //송신 문자를 전달
        check=1;
        break;
      }
     }
     a='0';
     if(check==1){                       //1분동안 진동신호가 있을때 스위치를 누르면 초록불3초간 켜주기
      digitalWrite(red,LOW);     
      digitalWrite(green,HIGH);
      delay(3000); 
      digitalWrite(green,LOW);
      check=0;
     }
    else digitalWrite(red,HIGH);         //1분간 신호 확인을 못하면 빨간불로 표시
   }
   else digitalWrite(vi,LOW);         //평상시 진동 끄기
   if(digitalRead(sw)==LOW) digitalWrite(red,LOW);      //스위치를 누르면 빨간불 끄기
}


//-------------------------------------함--------------수-----------------------------
//아래 for문은 진동5번,빨간LED깜빡이기 5번 수행 후 a는 0으로 설정
void Right_Vi(){
      digitalWrite(vi,HIGH);
      digitalWrite(red,LOW);
      delay(500);
      digitalWrite(vi,LOW);
      digitalWrite(red,HIGH);
      delay(500);  
}
