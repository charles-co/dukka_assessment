<template>
  <div class="container my-5">
    <figure class="animate__animated animate__fadeInUp">
      <blockquote class="blockquote text-success">
        <p class="h3">&OpenCurlyDoubleQuote; Programs must be written for people to read, and only incidentally for machines to execute &CloseCurlyDoubleQuote;</p>
      </blockquote>
      <figcaption class="blockquote-footer">
        <cite title="Source Title">by Harold Abelson and Gerald Jay Sussman</cite>
      </figcaption>
    </figure>
    <div class="row">
      <div class="col-sm-5">
        <h3>Github</h3>
      </div>
      <div class="col-sm-5">
        <h3>LinkedIn</h3>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'HomeScreen',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
