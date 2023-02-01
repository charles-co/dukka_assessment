<template>
    <footer class="footer">
        <div class="container-fluid">
            <p class="text-muted mb-0">&lt;/&gt; with ❤️, Charles</p>
        </div>
    </footer>
</template>

<script>
    export default {
        name: 'FooterBar',
        data() {
            return {
                currentYear: new Date().getFullYear()
            }
        }
    }
</script>

<style scoped>
.footer {
    background-color: #f5f5f5;
    padding: 20px;
    text-align: center;
    position: absolute;
    bottom: 0;
    width: 100%;
}
</style>
