import React from 'react'


const CustomUserItem = ({CustomUser}) => {
   return (
       <tr>
           <td>
               {CustomUser.firstname}
           </td>
           <td>
               {CustomUser.lastname}
           </td>
           <td>
               {CustomUser.email}
           </td>
       </tr>
   )
}

const CustomUserList = ({users}) => {
   return (
       <table>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               Email
           </th>
           {users.map((CustomUser) => <CustomUserItem CustomUser={CustomUser} />)}
       </table>
   )
}


export default CustomUserList