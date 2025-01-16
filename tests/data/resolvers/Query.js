function feed(parent, args, context) {
  return context.prisma.link.findMany();
}

function feedByCurrentUserId(parent, args, context) {
  const { userId } = context;

  if (!userId) {
    throw new Error("Authentication required to fetch user links.");
  }

  return context.prisma.user.findUnique({ where: { id: userId } }).links();
}

module.exports = {
  feed,
  feedByCurrentUserId,
};
