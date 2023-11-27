<template>
    <div class="post">
        <h2>Пост: {{ post.id }}</h2>
        <h4>Имя: {{ post.name }}</h4>
        <p>Описание: {{ post.description }}</p>
    </div>
</template>

<script>
export default {
    props : {
        post : {
            type: Object,
            required: true,
        }
    }
}
</script>

<style scoped>
.post {
    padding: 15px;
    border: 1px solid teal;
    margin-top: 15px;
}
</style>