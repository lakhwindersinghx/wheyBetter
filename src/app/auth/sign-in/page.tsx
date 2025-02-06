"use client"

import { signIn } from "next-auth/react"
import { useState } from "react"
import { useRouter } from "next/navigation"

export default function SignIn() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const router = useRouter()

  const handleSignIn = async (e: React.FormEvent) => {
    e.preventDefault()

    const result = await signIn("credentials", {
      redirect: false,
      email,
      password,
    })

    if (result?.ok) {
      router.push("/") // Redirect to homepage if successful
    } else {
      alert("Login failed. Please check your credentials.")
    }
  }

  return (
    <div className="flex h-screen justify-center items-center">
      <form onSubmit={handleSignIn} className="p-8 bg-gray-100 rounded-lg shadow-md space-y-4">
        <h2 className="text-2xl font-bold">Sign In</h2>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <button type="submit" className="w-full bg-blue-500 text-white py-2 rounded">
          Sign In
        </button>
      </form>
    </div>
  )
}