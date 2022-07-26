// Forma de usar las librerias usando ECMAScript
import express from "express";
import dotenv from "dotenv"


// buscara el archivo .env y seteara las variables dentro del archivo
    // como variable de entorno
dotenv.config()
// EcmaScript -> standar de uso de JS

// Babel -> compilador / transpilador que convierte de ECMAScript -> CommonJS
    // React Native utiliza internamente Babel


// forma de importar librerias usando Common.js
    // Common.js -> forma mas pura de usar JS
// const express=require("express");


// if(process.env.NODE_ENV==='development'){
//     // do something
// }

const PORT=process.env.PORT;
// 
const servidor=express()


servidor.get("/",(req,res)=>{
    res.json({
        message:"Hola"
    });
});

// servidor.listen(port,function)
    // ()=> anonym function
servidor.listen(PORT,()=>{
    console.log('Servidor corriendo exitosamenteeee en el puerto 3000')
})