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

const servidor=express()

const PORT=process.env.PORT;

servidor.use(express.json())
// 


const categories=[
    {
    name:'Zapatos',
    descripcion:'zapatos para hombres, mujeres y niñas.'
    },
];



servidor.get("/",(req,res)=>{
    res.status(200).json({
        message:"Wecolme to my first API"
    });
});

servidor.route("/categories")
    .get((req,res)=>{
        return res.status(200).json({categories})  
    })
    .post((req,res)=>{
        const category=req.body
        categories.push(category)
        return res.status(201).json({
            'message':'Created Sucsessfully.',
            'content':category
        })
    });

servidor.route("/categories/:id")
    .get((req,res)=>{
        const{id}=req.params;
        console.log(categories[id])
        if(categories[id]!==undefined){
            return res.json({
                'message':"la respuesta es",
                'content':categories[id]
            })
        }else{
            return res.status(400).json({
                'message':"la respuesta es",
                'content':null
            })
        }
        
    })

// Creacion de metodo

// servidor.listen(port,function)
    // ()=> anonym function
servidor.listen(PORT,()=>{
    console.log('Servidor corriendo exitosamenteeee en el puerto 3000')
})