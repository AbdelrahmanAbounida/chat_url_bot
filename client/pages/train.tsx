import React, {useState} from 'react'
import { useForm, SubmitHandler } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { toast } from 'react-hot-toast'
import Panels from '@/components/Panels'

import {z} from 'zod'
import Tabs from '@/components/Tabs'

const UrlPabel = () => {

    /* Handling Form elements */
  const [selectedTab, setselectedTab] = useState<string>('Text')

  // Data Sources
  const [botdata, setbotdata] = useState<string>()
  const [url, seturl] = useState<string>()

    const handleSubmit = (event:any) =>{
        console.log(url)
        event.preventDefault()

        if(!url && selectedTab== 'URL'){
            toast.error("Please enter a url before submitting")
        }
        else if(!botdata && selectedTab == 'Text'){
            toast.error("Please Enter your webpage content in text format before submitting")
        }
        else{
            toast.success("Data Conent Wil be stored now")
        }
        
        
    }

  return (


    <div className='mt-10 mx-auto  border-slate-500'>
         <form className='mt-12 xl:w-1/2  mx-4 lg:mx-auto items-center border border-slate-900 rounded pt-12' noValidate >

            {/* DATA SOURCES  */}

            <div className="sm:col-span-3 my-5 text-center">
                <label  className="block text-2xl text-center leading-6 text-teal-500 pl-2 font-inter">Data Source</label>
                <Tabs selectedTab={selectedTab} setselectedTab={setselectedTab}/>
            </div>

            <Panels  selectedTab={selectedTab}  setbotdata={setbotdata} url={url} seturl={seturl}/>

            {/* SUBMIT  */}
            <button onClick={handleSubmit} type='submit' className='mt-5 mb-10 mx-auto btn rounded bg-teal-600 text-white py-2 px-9 flex'>Submit</button>
            </form>

    </div>
  )
}

export default UrlPabel