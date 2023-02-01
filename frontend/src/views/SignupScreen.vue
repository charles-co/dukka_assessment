<template>
    <FormSlider type="signup" @formSubmitted="onFormSubmitted"/>
</template>

<script>
import FormSlider from '../components/FormSlider.vue';
import axiosInstance from '@/axios';

export default {
    name: 'SignupScreen',
    components: {
        FormSlider,
    },
    methods: {
        onFormSubmitted(event) {
            axiosInstance.post('/api/v1/', {
                "email": event.email,
                "password": event.password,
                "name": event.name,
                "sex": event.sex,
                "country": event.country,
                "phone_number": event.phone_number,
            }).then(response => {
                if (response.status === 201){
                    axiosInstance.post('/auth-token/', {
                        email: event.email,
                        password: event.password
                    }).then(response => {
                        localStorage.setItem('token', response.data.token);
                        this.$store.commit('setUserLoginStatus', true);
                        this.$router.push('/dashboard');
                    }).catch(error => {
                        console.log(error);
                    });
                }
                else {
                    this.$router.push('/signup');
                }
            }).catch(error => {
                console.log(error);
            });
        }
    },
}
</script>
