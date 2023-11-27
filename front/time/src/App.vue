<template>
    <div class="app">
        <post-form
        @create="createPost"/>
        <post-list :posts="posts"/>
    </div>

</template>


<script>
    import PostList from "@/components/PostList";
    import PostForm from "@/components/PostForm";
    export default {
    components: {
      PostList, PostForm

    },
    data() {
        return {
            posts : [{
                "id" : 1, "name" : "Test Name", "description" : "description dasdashdjkasjkdhasdhasjdas" 
            },{
                "id" : 2,
                "name" : "Test Name 2",
                "description" : "description dasdashdadslknfdsanfjkldsanfkjasdnjkasjkdhasdhasjdas"
            },{
                "id" : 3,
                "name" : "Test Name 3",
                "description" : "description adasdasdmkasdjkasmdksada"
            }]
        }
    }, 
    methods: {
        createPost(post) {
            this.posts.push(post);
        }
    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

#app {
    padding: 20px ;
}


</style>

