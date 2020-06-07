var ProjectInit = function(select_id){

  var select_obj = document.getElementById(select_id);
  // var options = "";

  function selectAddOption(select_obj,option_obj) {
    var option = document.createElement("option");
    // select_obj.options.add(new Option(option_obj.name,option_obj.pid));
    option.innerHTML = option_obj.name;
    option.value = option_obj.pid;
    select_obj.appendChild(option);  
  }
  function getProjectListInfo(){
    $.get("/project/get_project_list/",{},
      function(resp){
        alert("获取项目列表");
        if (resp.success == true && resp.status == 10200) {
          let pro_arr = resp.data
          for (let i = 0; i < pro_arr.length; i++) {
            selectAddOption(select_obj,pro_arr[i])
          }//for
          console.log(select_obj)
        }//if
      }//func
    );//get
  }//func

  getProjectListInfo();
}