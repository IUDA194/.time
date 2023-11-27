<template>
    <div class="main">
        <h1>Список постов</h1>
        <PostItem
        v-for="post in posts"
        :post="post"/>
    </div>
    
</template>

<script>
import PostItem from "@/components/PostItem";
export default {
    components: {
      PostItem
    },
    props: {
        posts : {
            type : Array,
            required : true
        }
    }
}
</script>

<style scoped>
</style>