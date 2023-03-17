
var Words = document.getElementById("words");
var Who = document.getElementById("who");
var TalkWords = document.getElementById("talkwords");
var TalkSub   = document.getElementById("talksub");
var Talkcon   = document.getElementById("talk_con");
var Talkref1         =document.getElementById("talkref1");
var Talkref2         =document.getElementById("talkref2");
var Talkref3         =document.getElementById("talkref3");
var Talkref4         =document.getElementById("talkref4");
var Talkref5         =document.getElementById("talkref5");
var Talkref6         =document.getElementById("talkref6");
var response_id = 100
$("#talkref1").click(function () {
    TalkWords.value = Talkref1.value;
    //TalkSub.click();

} )
$("#talkref2").click(function () {
    TalkWords.value = Talkref2.value;
    //TalkSub.click()
})
$("#talkref3").click(function () {
    TalkWords.value = Talkref3.value;

})
$("#talkref4").click(function () {
    TalkWords.value = Talkref4.value;
    //TalkSub.click()
})
$("#talkref5").click(function () {
    TalkWords.value = Talkref5.value;
    //TalkSub.click()
})
$("#talkref6").click(function () {
    TalkWords.value = Talkref6.value;
    //TalkSub.click()
})

$("#talksub").click(function () {

    //判断点击类型
     //定义空字符串
     var str = "";
     if( TalkWords.value == "" ){
          // 消息为空时弹窗
         alert("消息不能为空");
         return;
     }
     if (TalkWords.value.length >100)
     {
         alert('输入过长')
         return;
     }

     who.value = 1
     if(Who.value == 0){
         //如果Who.value为0n那么是 A说
         str = '<div class="atalk"> <span>' + TalkWords.value + '</span>   </div>';
     }
     else{
         str = '<div class="btalk"><span>' + TalkWords.value + '</span>  </div>' ;
     }
     Words.innerHTML = Words.innerHTML + str;
     Words.scrollTop = Words.scrollHeight  ;
   
    $.ajax({
        url: "/returnMessage",
        data: {
            "send_message": TalkWords.value
        },
        type: "Post",
        dataType: "text",
        success: function (data) {
            response_id = response_id+1;
            id_str      = 'id'+ response_id;
            console.log('id_str:',id_str);
            console.log('id_data**:',data);
            if (data =='wgnrnrwg')
            {
                tmp = '根据安全策略,不予置评';
                str2 = '<div class="atalk"><span>' +  tmp  +'</span></div>';
            }
            else
            {
            str = '<div class="atalk" id='+ id_str   +' <span>' + data +'</span> <button onclick="addclick_good('+ id_str + ')" id="resp_good" >满意√</button> <button onclick="addclick_bad('+ id_str + ')" id="resp_bad">不满意×</button>     </div>';
            str = str.replace('id_str','${id_str}')
            console.log('str *********:',str);
            var str2 = str.replace('id_str','${id_str}')
            console.log('str2 *********:',str2);
            }
            Words.innerHTML = Words.innerHTML + str2;
            Words.scrollTop = Words.scrollHeight  ;
        },
    })
    TalkWords.value = ""
})

function Send(){
        talksub.click();
        //alert("biz");
    }
    function addclick_good(inid) {
        console.log('inid:',inid);
        str =  inid.innerText.replace(' 满意√ 不满意×','')
        console.log('inid value:', str )
        //TalkWords.value = str;
         $.ajax(
            {
            url: "/feedback",
            data: {
                "send_message": str,
                'feedback': 'good'
                },
            type: "Post",
            dataType: "text"}
         )
    }
    function addclick_bad(inid) {
        console.log('inid:',inid);
        str =  inid.innerText.replace(' 满意√ 不满意×','')
        console.log('inid value:', str )
        $.ajax(
            {
            url: "/feedback",
            data:{
                "send_message": str,
                'feedback': 'bad'
                },
            type:    "Post",
            dataType: "text"}
         )


    }