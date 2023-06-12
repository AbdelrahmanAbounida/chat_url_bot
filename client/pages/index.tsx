import { useRouter } from "next/router"

export default function Home() {
  const router = useRouter()

  return (
    <div className="mx-auto px-10 w-full h-full py-12 my-12 xl:w-1/2 text-white ">

          <p className='text-center flex font-bold text-3xl justify-center mb-9'>CHAT <span className='text-teal-500'> WITH</span> Webpage</p>

      <div className="flex justify-between mx-auto w-1/2 mt-12 pt-12">
        <div className="border h-20 w-1/2 mx-2 flex items-center justify-center  rounded text-2xl border-teal-400 hover:border-teal-600 hover:shadow-lg">
          <button onClick={()=>{router.push('/train')}} className="btn  h-full w-full rounded-lg ">
            Train Bot
          </button>
        </div>

        <div className=" h-20 w-1/2 mx-2 flex items-center justify-center border rounded border-teal-400  text-2xl hover:border-teal-600 hover:shadow-lg transition">
          <button onClick={()=>{router.push('/chat')}} className="btn  rounded h-full w-full">
            Chat Bot
          </button>
        </div>
      </div>

      <div className="mt-12 border flex flex-col mx-auto border-slate-800 rounded-xl text-xl items-start text-center  justify-center h-28">
        <p className="text-white/80 "><span className="font-semibold text-teal-500  px-4">Train Bot:</span> Used to store webpage url content or regular text data to pinecone</p>
        <p className="text-white/80 "><span className="font-semibold text-teal-500 px-4 ">Chat Bot:</span> Used to chat with the content that bot has been trained on</p>

      </div>
    </div>
  )
}
