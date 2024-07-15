import React from 'react'

const ContactList = ({contacts}) => {
  return (
    <div>
        <h2>Contact List</h2>
        <table>
          <thead>
            <tr>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Email</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {contacts.map(contact => (
              <tr key={contact.id}>
                <td>{contact.firstName}</td>
                <td>{contact.lastName}</td>
                <td>{contact.email}</td>
                <td>
                  <button onClick={() => console.log('Edit contact')}>Edit</button>
                  <button onClick={() => console.log('Delete contact')}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
  </div>
  )
}

export default ContactList
