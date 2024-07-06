'use client'
import CarouselIIT from './IITCarousel';
import {ArrowRight} from 'lucide-react'

export default function Home() {
  return (
    <>
      
      <div class="pt-32 md:py-12 xl:container m-auto px-6 md:px-12 h-screen w-screen">
          <div aria-hidden="true" class="absolute inset-0 my-auto w-96 h-32 rotate-45 bg-gradient-to-r from-primaryLight to-secondaryLight blur-3xl opacity-50 dark:opacity-20"></div>
          <div class="relative lg:flex lg:items-center lg:gap-12">
              <div class="text-center lg:text-left md:mt-12 lg:mt-0 sm:w-10/12 md:w-2/3 sm:mx-auto lg:mr-auto lg:w-6/12">
                  <h1 class="text-gray-900 font-bold text-4xl md:text-6xl lg:text-5xl xl:text-6xl dark:text-white">Empowering your future with expert career <span class="text-primary dark:text-primaryLight">Guidance.</span></h1>
                  <p class="mt-8 text-gray-600 dark:text-gray-300">RankIt is a comprehensive JoSAA rank analyzer designed to assist students in evaluating their chances of admission into various IITs, NITs, and other prestigious institutions. By inputting their rank, students can receive personalized insights and recommendations on the best colleges and courses available to them. This tool helps in making informed decisions during the counseling process.</p>
                  <div class="mt-16 space-y-2 lg:space-y-0 md:w-max sm:space-x-6">
                    <button type="button" title="Start buying" class="w-full py-3 px-6 text-center rounded-full transition bg-slate-900 text-white dark:text-black dark:hover:bg-slate-200 dark:bg-slate-50 hover:bg-slate-700 active:bg-slate-400 focus:bg-slate-300 sm:w-max">
                        <span class="block text-white dark:text-black font-semibold text-sm">
                            Get Started <ArrowRight/>
                            
                        </span>
                        
                    </button>
                      </div>
                  <div class="mt-12 flex gap-6 lg:gap-12 justify-center grayscale dark:grayscale-0">
                      <CarouselIIT/>
                  </div>
              </div>
          </div>
      </div> 
                                    
    </>
  );
}

