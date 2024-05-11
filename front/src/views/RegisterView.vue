<template>
    <div>
    <h1>Регистрация</h1>
    <v-form @submit.prevent>
      <v-text-field
        v-model="user.username"
        label="Логин"
      ></v-text-field>
      <v-text-field
        v-model="user.email"
        label="Email"
      ></v-text-field>
      <v-text-field
        v-model="user.pwd"
        label="Пароль"
      ></v-text-field>
      <v-text-field
        v-model="user.pwd"
        label="Пароль"
      ></v-text-field>
      <v-text-field
        v-model="user.birthday"
        label="День рождения"
      ></v-text-field>
      <v-btn class="mt-2" type="submit" block @click="send">Регистрация</v-btn>
    </v-form>
    </div>
</template>


<script>
 export default {
    methods:{
        send(){
            this.axios.post("http://127.0.0.1:8000/reg",this.user).then(data=>{
                console.log(data)
                this.$toast.open({
                message: 'Регистрация успешна',
                type: 'success',
                });
            }).catch(data=>{
                console.log(data)
                this.$toast.open({
                message: 'Ошибка валидации',
                type: 'error',
                });
            })
            
        }
    },
    data: () => ({
      user:{
        username:null,
        email:null,
        pwd:null,
        birthday:null
      }
    }),
 }
</script>

