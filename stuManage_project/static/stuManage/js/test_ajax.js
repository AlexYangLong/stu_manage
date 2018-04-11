$(document).ready(function () {
    alert('12345')
    $('#btn-login').click(function () {
        //alert('2222')
        var name = $('#name').val();
        var pass = $('#pass').val();
        var csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val()

        $.ajax({
            url: "{% url 'stuManage:TestAJAX' %}",
            data: {'name': name, 'pass':pass, 'csrfmiddlewaretoken': csrfmiddlewaretoken},
            type:'POST',
            dataType:'json',
            success:function(data,textStatus){
                alert(data);
                alert(textStatus)
            },
            error:function(e){

            }
        })

        alert(name + " " + pass)
    });

});