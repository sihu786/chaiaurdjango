
const bt=document.getElementById('bt')
bt.addEventListener('click',(e)=>{
  let name=document.getElementById('name').value;
  let email=document.getElementById('email').value;
  let sub=document.getElementById('subject').value;
  let mes=document.getElementById('message').value;

  let body="Name: " + name + "<br/> Email: " + email + "<br/> Subject: " + sub + "<br/> Message: " + mes + "<br/>"



  e.preventDefault()

  Email.send({
    SecureToken : "77b3b9d7-4698-4e30-9fdc-9461b7b8b694 ",
    
    To : 'bikramadak15@gmail.com',
    From : 'bikramadak15@gmail.com',
    Subject : sub,
    Body : body,
}).then(
  message => {
    if(message=='OK'){
      swal("Successfull", "Your Data is Successfull Recived!", "success");

    }else{
      swal("Somthing Wrong", "Your Data Not Recived!", "error");

    }

  }
);

// 77b3b9d7-4698-4e30-9fdc-9461b7b8b694 

 



})