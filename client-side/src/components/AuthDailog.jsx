'use client'


import AuthView from "@/app/auth/AuthView"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from "react"

const AuthDailog = () => {
    const [mode, setMode] = useState('sign_in')
  return (
    <>
        <Dialog className="relative z-50 p-2 min-w-50" >
            <DialogTrigger asChild>
                <div class="w-full space-y-2 border-primary/10 dark:border-gray-700 flex flex-col ml-1 sm:flex-row lg:space-y-0 md:w-max lg:border-l">
                    <Button onClick={() => setMode('sign_up')} class="relative flex h-9 ml-auto items-center justify-center sm:px-6 before:absolute before:inset-0 before:rounded-full focus:before:bg-primary/10 dark:focus:before:bg-primaryLight/10 before:transition before:duration-300 hover:before:scale-105 active:duration-75 active:before:scale-95">
                        <span class="relative text-sm font-semibold text-primary dark:text-primaryLight">Sign Up</span>                    
                    </Button>
                    <Button onClick={() => setMode('sign_in')} class="relative flex h-9 ml-auto items-center justify-center sm:px-6 before:absolute before:inset-0 before:rounded-full before:bg-primary dark:before:bg-primaryLight before:transition before:duration-300 hover:before:scale-105 active:duration-75 active:before:scale-95">
                        <span class="relative text-sm font-semibold text-white dark:text-gray-900">Login</span>                    
                    </Button>
                </div>
            </DialogTrigger>
            <DialogContent className="sm:max-w-[425px]">
                <AuthView mode={mode}/>
            </DialogContent>
        </Dialog>
    </>
  )
}

export default AuthDailog