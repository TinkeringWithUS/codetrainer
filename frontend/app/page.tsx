"use client";

import Image from "next/image";
import { useEffect } from "react";

import {backendGetJSON} from "@/app/api/backend";

export default function Home() {
  // useEffect(() => {
  //   console.log(backendGetJSON()) 
  
  //   return () => {
      
  //   }
  // }, []);

  useEffect(() => {
    backendGetJSON()
      .then((res) => console.log(res))
  
    return () => {
      
    }
  }, [])
  

  return (
    <div>
      hi
    </div>
  )
}
  

