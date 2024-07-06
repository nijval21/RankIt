import * as React from "react";
import { Card, CardContent } from "@/components/ui/card";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import Image from "next/image";
import IITKGP from '@/assets/iitkgp.png';
import iitd from '@/assets/iitd.png';
import iitk from '@/assets/iitk.png';
import iith from '@/assets/iith.png';
import iitm from '@/assets/iitm.png';
import iitv from '@/assets/iitv.png';

export function CarouselIIT() {
  return (
    <Carousel className="w-full">
      <CarouselContent>
        <CarouselItem key={1} className="border-0 md:basis-1/2 lg:basis-1/3">
          <div className="">
            <Card>
              <CardContent className="flex aspect-square items-center justify-center ">
                <Image src={IITKGP} alt="IIT Kharagpur" className="grayscale-0 dark:grayscale-0" />
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
        <CarouselItem key={2} className="border-0 md:basis-1/2 lg:basis-1/3 sm:basis-1">
          <Card>
            <CardContent className="flex aspect-square items-center justify-center border-0">
              <Image src={iitd} className="w-60 grayscale-0 dark:grayscale-0" alt="IIT Delhi" />
            </CardContent>
          </Card>
        </CarouselItem>
        <CarouselItem key={3} className="border-0 md:basis-1/2 lg:basis-1/3">
          <div className="">
            <Card>
              <CardContent className="flex aspect-square items-center justify-center ">
                <Image src={iitm} alt="IIT Madras" className="grayscale-0 dark:grayscale-0"/>
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
        <CarouselItem key={4} className="border-0 md:basis-1/2 lg:basis-1/3">
          <div className="">
            <Card>
              <CardContent className="flex aspect-square items-center justify-center ">
                <Image src={iitv} alt="IIT Varanasi" className="grayscale-0 dark:grayscale-0"/>
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
        <CarouselItem key={5} className="border-0 md:basis-1/2 lg:basis-1/3">
          <div className="">
            <Card>
              <CardContent className="flex aspect-square items-center justify-center ">
                <Image src={iith} alt="IIT Hyderabad" className="grayscale-0 dark:grayscale-0" />
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
        <CarouselItem key={6} className="border-0 md:basis-1/2 lg:basis-1/3">
          <div className="">
            <Card>
              <CardContent className="flex aspect-square items-center justify-center ">
                <Image src={iitk} alt="IIT Kanpur" className="grayscale-0 dark:grayscale-0" />
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious />
      <CarouselNext />
    </Carousel>
  );
}

export default CarouselIIT;