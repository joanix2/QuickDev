const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { APP_SECRET } = require("./utils");

function post(parent, args, context) {
  const { userId } = context;

  if (!userId) {
    throw new Error("Authentication required to create a new link.");
  }

  const { url, description } = args;

  const newLink = context.prisma.link.create({
    data: {
      url,
      description,
      postedBy: { connect: { id: userId } },
    },
  });

  return newLink;
}

async function signup(parent, args, context) {
  const password = await bcrypt.hash(args.password, 10);

  const user = await context.prisma.user.create({
    data: { ...args, password },
  });

  const token = jwt.sign({ userId: user.id }, APP_SECRET);

  return {
    token,
    user,
  };
}

async function login(parent, args, context) {
  const user = await context.prisma.user.findUnique({
    where: { email: args.email },
  });

  if (!user) {
    throw new Error("No such user found");
  }

  const valid = await bcrypt.compare(args.password, user.password);

  if (!valid) {
    throw new Error("Invalid password");
  }

  const token = jwt.sign({ userId: user.id }, APP_SECRET);

  return {
    token,
    user,
  };
}

module.exports = {
  post,
  login,
  signup,
};
