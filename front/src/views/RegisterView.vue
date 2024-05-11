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
            console.log(1)
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

