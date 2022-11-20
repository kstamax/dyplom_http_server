const BASE_API_URL = `api/doorlogs`
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
                if(list[i]['door_state'] === 'opened'){
                    text_color='text-success'
                }
                else{
                    text_color='text-danger'
                } 
                var item = `
                <li class="list-group-item ${text_color}">${list[i]['log_date']}  ${list[i]['door_state']}</li>
                `;
                console.log(list)
                lst.innerHTML += item;
                console.log(list.innerHTML)
            }
        })
    }