const base = {
    get() {
        return {
            url : "http://localhost:8080/djangozo3p7/",
            name: "djangozo3p7",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/h5/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于微信平台小区服务系统"
        } 
    }
}
export default base
