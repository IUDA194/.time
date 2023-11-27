<template>
    <form @submit.prevent>
        <h2>Add new post</h2>
        <input 
        v-model="posts.name"
        class="input"
        type="text" 
        placeholder="Name">
        <input 
        v-model="posts.description"
        class="input"
        type="text" 
        placeholder="description">
        <button class="btn" @click="createPost">Create post</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            posts : {
                name : "",
                description : ""
            }
        }
    }, 
    methods: {
        createPost() {
            this.posts.id = Date.now()
            this.$emit("create", this.posts)
            this.posts = {
                name : "",
                description : ""
            }
        }
    }
    
};
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
}

.input {
    width: 100%;
    border: 1px solid teal;
    padding: 10px 15px;
    margin-top: 5px;
}

.btn {
    align-self: flex-end;
    margin-top: 15px;
    border: 1px solid teal;
    padding: 10px 15px;
    background: none;
    color: teal;
}
</style>