import React from 'react'



const UrlPabel = ({url,seturl}:any) => {

  return (


    <div className='mt-10 mx-auto border-slate-500'>

        {/* URL */}
        <div className="sm:col-span-3 mt-5 mx-10">
            <label  className="block text-xl text-start leading-6 text-teal-600 pl-2 font-inter">URL <span className='text-start text-gray-400/60 pl-0 text-lg mt-2'></span></label>
            
            <div className="mt-2">
                <input 
                type="text" className={` border-slate-600/30 block w-full bg-[#101010] hover:ring-slate-600/40 hover:ring-[0.07rem] text-white/90 border px-2  shadow-sm rounded-xl placeholder:text-gray-400/60 placeholder:text-sm py-2  !outline-none `} 
                placeholder='Enter Your webpage URL here. for now only static webpage or site.xml will be scraped'
                onChange={e => seturl(e.target.value)}
                value={url}
                />
            </div>
        </div>




    </div>
  )
}

export default UrlPabel