import { NextResponse } from "next/server"
import prisma from "@/app/dbConfig/dbConfig" // Updated import path
import bcrypt from "bcryptjs"

export async function POST(req: Request) {
  try {
    const { email,username, password } = await req.json()

    const existingUser = await prisma.user.findUnique({
      where: { email },
    })

    if (existingUser) {
      return NextResponse.json({ error: "User already exists." }, { status: 400 })
    }

    const hashedPassword = await bcrypt.hash(password, 10)

    const user = await prisma.user.create({
      data: {
        email,
        username,
        password: hashedPassword,
      },
    })

    return NextResponse.json({ message: "User created successfully" }, { status: 201 })
  } catch (error) {
    console.error("Signup error:", error)
    return NextResponse.json({ error: "Something went wrong." }, { status: 500 })
  }
}

