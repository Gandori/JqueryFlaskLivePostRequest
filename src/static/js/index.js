
$("#submit").click( () => 
{
    const name = document.getElementById("name")
    const pwd =document.getElementById("pwd")    
    if(!name.value || !pwd.value){input_empty(name, pwd);return;}
    post(name.value, pwd.value);
})

function post(name, pwd)
{
    console.log(true);
    $.ajax(
    {
        url:"login",
        type:"POST",
        data:{
           "name":name,
           "pwd":pwd
        },
        success:function(res)
        {
            $("#message").html(res);
        }
    });
}

function input_empty()
{
    const h = document.getElementById("message")
    h.innerHTML = "All fields must be filled"
    document.querySelector("body").append(h);
}
