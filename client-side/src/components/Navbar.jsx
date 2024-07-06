'use client'
import {useState,useEffect} from 'react'
import { ModeToggle } from './toggleTheme'
const Navbar = () => {
  return (
    <>
        <header>
          <input type="checkbox" name="hbr" id="hbr" class="hbr peer" hidden aria-hidden="true"/>
          <nav class="fixed z-20 w-full bg-white/80 dark:bg-gray-900/80 backdrop-blur navbar shadow-md shadow-gray-600/5 peer-checked:navbar-active md:relative md:bg-transparent dark:shadow-none">
              <div class="xl:container m-auto px-6 md:px-12">
                  <div class="flex flex-wrap items-center justify-between gap-6 md:py-3 md:gap-0">
                      <div class="w-full flex justify-between lg:w-auto">
                          <a href="#" aria-label="logo" class="flex space-x-2 items-center">
                              <div aria-hidden="true" class="flex space-x-1">
                                  <div class="h-4 w-4 rounded-full bg-gray-900 dark:bg-gray-200"></div>
                                  <div class="h-6 w-2 bg-primary dark:bg-primaryLight"></div>
                              </div>
                              <span class="text-base font-bold text-gray-600 dark:text-white ml-1">GuideU</span>
                          </a>
                          <label for="hbr" class="peer-checked:hamburger block relative z-20 p-6 -mr-6 cursor-pointer lg:hidden">
                              <div aria-hidden="true" class="m-auto h-0.5 w-6 rounded bg-gray-900 dark:bg-gray-300 transition duration-300"></div>
                              <div aria-hidden="true" class="m-auto mt-2 h-0.5 w-6 rounded bg-gray-900 dark:bg-gray-300 transition duration-300"></div>
                          </label>
                      </div>
                      
                      <div class="navmenu hidden w-auto flex-wrap justify-end items-center mb-16 space-y-8 p-6 border border-gray-100 rounded-3xl shadow-2xl shadow-gray-300/20 bg-white dark:bg-gray-800 lg:space-y-0 lg:p-0 lg:m-0 lg:flex md:flex-nowrap lg:bg-transparent lg:w-7/12 lg:shadow-none dark:shadow-none dark:border-gray-700 lg:border-0">
                          <ModeToggle/>
                          <div class="text-gray-600 dark:text-gray-300 lg:pr-4">
                              <ul class="space-y-6 tracking-wide font-medium text-base lg:text-sm lg:flex lg:space-y-0">
                                  <li>
                                      <div onClick={() => router.push('/home')} class="block md:px-4 transition hover:text-primary dark:hover:text-primaryLight">
                                          <span>Home</span>
                                      </div>
                                  </li>
                                  <li>
                                      <div onClick={() => router.push('/news')} class="block md:px-4 transition duration-200 hover:text-primary hover:cursor-pointer hover:dark:hover:text-primaryLight">
                                          <span>News</span>
                                      </div>
                                  </li>
                                  <li>
                                      <a href="#" class="block md:px-4 transition hover:text-primary dark:hover:text-primaryLight">
                                          <span>About Us</span>
                                      </a>
                                  </li>
                              </ul>
                          </div>
                        
                            
                                <AuthDailog/>
                
                    
                      </div>
                  </div>
              </div>
          </nav>
      </header>
    </>

  )
}

export default Navbar