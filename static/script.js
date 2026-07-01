async function sendMessage(){

let input=document.getElementById("message");

let text=input.value;

let chat=document.getElementById("chatbox");

chat.innerHTML += "<p class='user'><b>You:</b> "+text+"</p>";

input.value="";

let response=await fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:text
})

});

let data=await response.json();

chat.innerHTML += "<p class='bot'><b>AI:</b> "+data.response+"</p>";

chat.scrollTop=chat.scrollHeight;

}