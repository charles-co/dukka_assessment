<!-- This is the navbar component. It is used in the App.vue file.
    It has a logo, a home button, a dashboard button, a login button, and a signup button.
    The dashboard button and the logout button are only visible when the user is logged in.
    The login and signup buttons are only visible when the user is not logged in.
 -->
<template>
    <div class="mb-1">
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <div class="container-fluid">
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <router-link class="navbar-brand" to="/">
                    <img src="../assets/logo.png" class="img-responsive" width="100" height="30" alt="logo">
                </router-link>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <router-link class="nav-link" to="/">Home</router-link><span class="visually-hidden">(current)</span>
                        </li>
                        <template v-if="isLoggedIn">
                            <li class="nav-item">
                                <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
                            </li>
                            <li class="nav-item">
                                <button class="btn btn-danger" @click="logout">Log out</button>
                            </li>
                        </template>
                        <template v-else>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/login">Log in</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/signup">Sign up</router-link>
                            </li>
                        </template>
                    </ul>
                </div>
            </div>
        </nav>

    </div>

</template>

<script>

export default {
    name: 'NavBar',
    props: {},
    computed: {
        isLoggedIn() {
            return this.$store.state.isLoggedin;
        },
    },
    methods: {
        logout() {
            localStorage.removeItem('token');
            this.$store.commit('setUserLoginStatus', false);
            this.$router.push('/login');
        },
    },
    created() {
        if (localStorage.getItem('token')) {
            this.$store.commit('setUserLoginStatus', true)
        }
    }
}
</script>
