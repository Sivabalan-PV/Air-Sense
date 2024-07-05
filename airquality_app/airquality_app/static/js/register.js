console.log("register working")
const usernameField=document.querySelector('#usernameField');
const feedbackArea=document.querySelector('.invalid_feedback');

usernameField.addEventListener("keyup", (e) => {
    console.log('777777',777777);
    const  usernameval =e.target.value;

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display="none" ;

if(usernameval.length > 0){
    fetch("/authentication/validate_user",{
        body:JSON.stringify({username:usernameval}),
        method:"POST",
    }).then(res=>res.json()).then(data=>{
        console.log("data",data);
        if(data.username_error){
            usernameField.classList.add("is-invalid");
            feedbackArea.style.display="block" ;
            feedbackArea.innerHTML=`<p>${data.username_error}</p>`

        }
    });
}
});