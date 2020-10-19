// 插入内容到选择框
function selectAddOption(select_obj,option_obj) {
  var option = document.createElement("option");
  // select_obj.options.add(new Option(option_obj.name,option_obj.pid));
  option.innerHTML = option_obj.name;
  option.value = option_obj.id;
  select_obj.appendChild(option);  
}

// 清理下拉选项
function clearOption(select_obj){
  select_obj.options.length=0;  
  console.log("清除下拉选项");
  // for (let i = 0; i < select_obj.length; i++) {
  //   console.log("清除下拉选项",select_obj[i]);
  //   select_obj.options.remove(select_obj[i]);
  // }
}

var ModuleInit = function(module_select_id,pid){
  // 定位模块选择框
  var select_obj = document.getElementById(module_select_id);
  console.log("模块选择框:",select_obj)

  function getModuleListInfo(){
    // 请求后端返回该项目下的模块列表
    $.post("/module/get_module_list/",
      {
        "pid":pid,
      },
      function(resp){
        if (resp.success == true && resp.status == 10200) {
          let mod_arr = resp.data
          clearOption(select_obj)
          for (let i = 0; i < mod_arr.length; i++) {
            selectAddOption(select_obj,mod_arr[i])
          }//for
          // $("#module_arr").selectpicker("refresh");
          console.log(select_obj)
        }//if
        else { window.alert(resp.data)}
      }//func
    );//post
  }//func

  // 请求后端返回模块列表 并将数据插入前端选择框内
  getModuleListInfo();
}

var ProjectInit = function(project_select_id){
  // 定位项目选择框
  var select_obj = document.getElementById(project_select_id);
  // var options = "";

  function getProjectListInfo(){
    $.get("/project/get_project_list/",{},
      function(resp){
        alert("获取项目列表");
        if (resp.success == true && resp.status == 10200) {
          let pro_arr = resp.data
          for (let i = 0; i < pro_arr.length; i++) {
            selectAddOption(select_obj,pro_arr[i])
          }//for
          // console.log(select_obj)
        }//if
        else { window.alert(resp.data)}
      }//func
    );//get
  }//func

  // 请求后端返回项目列表 并将数据插入前端选择框内
  getProjectListInfo();
}

