const BASE_API_URL = `api/devicelogs`
    buildTable();
    function buildTable(){
        var lst = document.getElementById("itemsList");
        lst.innerHTML = '';
        var url = BASE_API_URL;
        fetch(url)
        .then((resp)=>resp.json())
        .then(function(data){
            var list = data;
            for (var i in list){
                text_color = ''
                if(list[i]['message_type'] === 'INFO'){
                    text_color='text-primary'
                }
                else{
                    text_color='text-danger'
                } 
                var item = `
                <li class="list-group-item ${text_color}">${list[i]['message_type']}    ${list[i]['log_date']}    ${list[i]['message_body']}</li>
                `;
                lst.innerHTML += item;
            }
        })
    }
    setInterval(function(){ 
        liveUpdate()   
    }, 2000);
    function liveUpdate(){
        var lst = document.getElementById("itemsList");
        var url = BASE_API_URL;
        fetch(url)
        .then((resp)=>resp.json())
        .then(function(data){
            var list = data;
            for (var i in list){
                text_color = ''
                if(list[i]['message_type'] === 'INFO'){
                    text_color='text-primary'
                }
                else{
                    text_color='text-danger'
                } 
                var item = `
                <li class="list-group-item ${text_color}">${list[i]['message_type']}    ${list[i]['log_date']}    ${list[i]['message_body']}</li>
                `;
                if(!lst.innerHTML.includes(item)){
                    lst.innerHTML = item + lst.innerHTML;
                }
            }
        })
    }